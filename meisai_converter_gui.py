#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
クレジットカード明細から確定申告用CSVを生成するツール（GUI版）
"""

import csv
import re
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from datetime import datetime
import threading


class MeisaiConverter:
    """クレカ明細を確定申告用フォーマットに変換"""

    def __init__(self, target_year):
        self.target_year = target_year
        self.records = []

    def parse_date(self, date_str):
        """日付文字列をパース (例: 251013 -> 2025/10/13)"""
        if not date_str or len(date_str) < 6:
            return None

        try:
            year = int(date_str[:2])
            month = int(date_str[2:4])
            day = int(date_str[4:6])
            full_year = 2000 + year
            return f"{full_year}/{month}/{day}", full_year
        except:
            return None

    def process_file(self, input_path):
        """CSVファイルを処理"""
        try:
            with open(input_path, 'r', encoding='shift-jis') as f:
                reader = csv.reader(f)
                data_section = False
                for row in reader:
                    if not row:
                        continue

                    if len(row) > 0 and row[0] and re.match(r'^\d{6}$', str(row[0])):
                        data_section = True

                    if data_section and len(row) >= 8:
                        date_str = row[0]
                        store = row[2] if len(row) > 2 else ""
                        amount = row[6] if len(row) > 6 else ""
                        note = row[7] if len(row) > 7 else ""

                        parsed = self.parse_date(date_str)
                        if not parsed:
                            continue

                        formatted_date, year = parsed

                        if year == self.target_year:
                            try:
                                amount_int = int(amount) if amount else 0
                                if amount_int > 0:
                                    self.records.append({
                                        '日付': formatted_date,
                                        '利用金額': amount_int,
                                        '返金額': '',
                                        '内容': store
                                    })
                            except ValueError:
                                continue
            return True
        except Exception as e:
            return False

    def save_output(self, output_path):
        """結果をCSVファイルに保存"""
        if not self.records:
            return False

        try:
            self.records.sort(key=lambda x: datetime.strptime(x['日付'], '%Y/%m/%d'))
            with open(output_path, 'w', encoding='utf-8-sig', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['日付', '利用金額', '返金額', '内容'])
                writer.writeheader()
                writer.writerows(self.records)
            return True
        except Exception as e:
            return False


class ConverterGUI:
    """GUIアプリケーション"""

    def __init__(self, root):
        self.root = root
        self.root.title("クレカ明細変換ツール")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.input_files = []
        self.setup_ui()

    def setup_ui(self):
        """UIをセットアップ"""
        # ヘッダー
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)

        title_label = tk.Label(
            header_frame,
            text="クレジットカード明細 → 確定申告用CSV",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(pady=25)

        # メインフレーム
        main_frame = tk.Frame(self.root, padx=30, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 対象年入力
        year_frame = tk.Frame(main_frame)
        year_frame.pack(fill=tk.X, pady=(0, 20))

        tk.Label(year_frame, text="対象年:", font=("Arial", 11)).pack(side=tk.LEFT, padx=(0, 10))

        self.year_var = tk.StringVar(value=str(datetime.now().year))
        year_spinbox = tk.Spinbox(
            year_frame,
            from_=2020,
            to=2030,
            textvariable=self.year_var,
            width=10,
            font=("Arial", 11)
        )
        year_spinbox.pack(side=tk.LEFT)

        # ファイル選択
        file_frame = tk.Frame(main_frame)
        file_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            file_frame,
            text="入力CSVファイル:",
            font=("Arial", 11)
        ).pack(anchor=tk.W, pady=(0, 5))

        # ファイルリスト
        list_frame = tk.Frame(file_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 10),
            yscrollcommand=scrollbar.set,
            height=8
        )
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_listbox.yview)

        # ファイル操作ボタン
        button_frame = tk.Frame(file_frame)
        button_frame.pack(fill=tk.X, pady=(0, 20))

        tk.Button(
            button_frame,
            text="📁 ファイルを追加",
            command=self.add_files,
            font=("Arial", 10),
            bg="#3498db",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=8
        ).pack(side=tk.LEFT, padx=(0, 10))

        tk.Button(
            button_frame,
            text="🗑️ 選択を削除",
            command=self.remove_file,
            font=("Arial", 10),
            bg="#e74c3c",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=8
        ).pack(side=tk.LEFT, padx=(0, 10))

        tk.Button(
            button_frame,
            text="🗑️ すべてクリア",
            command=self.clear_files,
            font=("Arial", 10),
            bg="#95a5a6",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=8
        ).pack(side=tk.LEFT)

        # 変換ボタン
        self.convert_button = tk.Button(
            main_frame,
            text="🔄 変換を実行",
            command=self.start_conversion,
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            relief=tk.FLAT,
            padx=40,
            pady=12
        )
        self.convert_button.pack(pady=(0, 10))

        # ステータスバー
        self.status_label = tk.Label(
            main_frame,
            text="ファイルを追加して、変換を実行してください",
            font=("Arial", 9),
            fg="#7f8c8d"
        )
        self.status_label.pack()

    def add_files(self):
        """ファイルを追加"""
        files = filedialog.askopenfilenames(
            title="CSVファイルを選択",
            filetypes=[("CSVファイル", "*.csv"), ("すべてのファイル", "*.*")]
        )

        for file in files:
            if file not in self.input_files:
                self.input_files.append(file)
                self.file_listbox.insert(tk.END, os.path.basename(file))

        self.update_status()

    def remove_file(self):
        """選択されたファイルを削除"""
        selection = self.file_listbox.curselection()
        if selection:
            index = selection[0]
            self.file_listbox.delete(index)
            del self.input_files[index]
            self.update_status()

    def clear_files(self):
        """すべてのファイルをクリア"""
        self.file_listbox.delete(0, tk.END)
        self.input_files.clear()
        self.update_status()

    def update_status(self):
        """ステータスを更新"""
        if self.input_files:
            self.status_label.config(
                text=f"{len(self.input_files)}個のファイルが選択されています"
            )
        else:
            self.status_label.config(
                text="ファイルを追加して、変換を実行してください"
            )

    def start_conversion(self):
        """変換を開始"""
        if not self.input_files:
            messagebox.showwarning("警告", "CSVファイルを選択してください")
            return

        try:
            year = int(self.year_var.get())
        except ValueError:
            messagebox.showerror("エラー", "有効な年を入力してください")
            return

        # 保存先を選択
        output_file = filedialog.asksaveasfilename(
            title="保存先を選択",
            defaultextension=".csv",
            initialfile=f"output_{year}.csv",
            filetypes=[("CSVファイル", "*.csv"), ("すべてのファイル", "*.*")]
        )

        if not output_file:
            return

        # 変換を実行
        self.convert_button.config(state=tk.DISABLED)
        self.status_label.config(text="変換中...")

        thread = threading.Thread(
            target=self.run_conversion,
            args=(year, output_file)
        )
        thread.start()

    def run_conversion(self, year, output_file):
        """変換処理を実行"""
        converter = MeisaiConverter(year)

        success_count = 0
        for input_file in self.input_files:
            if converter.process_file(input_file):
                success_count += 1

        if success_count > 0 and converter.records:
            if converter.save_output(output_file):
                self.root.after(
                    0,
                    lambda: self.show_success(
                        len(converter.records),
                        output_file
                    )
                )
            else:
                self.root.after(
                    0,
                    lambda: messagebox.showerror(
                        "エラー",
                        "出力ファイルの保存に失敗しました"
                    )
                )
        else:
            self.root.after(
                0,
                lambda: messagebox.showwarning(
                    "警告",
                    f"{year}年のデータが見つかりませんでした"
                )
            )

        self.root.after(0, self.reset_ui)

    def show_success(self, record_count, output_file):
        """成功メッセージを表示"""
        messagebox.showinfo(
            "完了",
            f"変換が完了しました！\n\n"
            f"件数: {record_count}件\n"
            f"出力: {os.path.basename(output_file)}"
        )
        # ファイルの場所を開く
        if messagebox.askyesno("確認", "出力フォルダを開きますか？"):
            os.startfile(os.path.dirname(output_file))

    def reset_ui(self):
        """UIをリセット"""
        self.convert_button.config(state=tk.NORMAL)
        self.update_status()


def main():
    """メイン処理"""
    root = tk.Tk()
    app = ConverterGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
