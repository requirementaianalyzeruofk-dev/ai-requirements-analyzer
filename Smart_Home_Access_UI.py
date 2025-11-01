import tkinter as tk
from tkinter import ttk
from db_manager import get_requirements

# إعداد نافذة الواجهة (The main window)
root = tk.Tk()
root.title("Smart Home Access UI - Requirement Analysis")

root.geometry("1000x550")
root.resizable(False, False)

# جلب البيانات من قاعدة البيانات
requirements = get_requirements()

# إعداد عرض الشجرة (Treeview)
tree = ttk.Treeview(root, columns=(
    "ID", "Text", "Functional", "Ambiguous", "Measurable", "Notes"
), show="headings")

# تحديد عرض الأعمدة
tree.column("ID", width=30, anchor="center")
tree.column("Text", width=350, anchor="w")
tree.column("Functional", width=80, anchor="center")
tree.column("Ambiguous", width=80, anchor="center")
tree.column("Measurable", width=80, anchor="center")
tree.column("Notes", width=300, anchor="w")

# تحديد عناوين الأعمدة
tree.heading("ID", text="ID")
tree.heading("Text", text="Requirement Text (النص)")
tree.heading("Functional", text="Functional")
tree.heading("Ambiguous", text="Ambiguous")
tree.heading("Measurable", text="Measurable")
tree.heading("Notes", text="Notes (ملاحظات)")

# إدخال البيانات في الجدول
for req in requirements:
    func_text = "✅ Yes" if req["functional"] else "❌ No"
    amb_text = "❌ Yes" if req["ambiguous"] else "✅ No"
    meas_text = "✅ Yes" if req["measurable"] else "❌ No"
    
    tree.insert("", tk.END, values=(
        req["id"],
        req["text"],
        func_text,
        amb_text,
        meas_text,
        req["notes"]
    ))

# إضافة شريط التمرير (Scrollbar)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# وضع الجدول وشريط التمرير في الواجهة
tree.pack(fill="both", expand=True, padx=10, pady=10)
scrollbar.pack(side="right", fill="y")

# تشغيل حلقة الواجهة الرئيسية (هذا هو السطر الذي يشغل النافذة)
root.mainloop()