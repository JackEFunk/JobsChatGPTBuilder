import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def generate_resume():
    res = tk.Toplevel(window)
    res.geometry("750x250")
    res.title("Resume Text")
    txt_paste = tk.Text(res)
    txt_paste.insert(1.0, 'Please rewrite my resume for this ' + entry_job.get() + ' role at ' + entry_comp.get() +
                     '.\nHere is the job description: ' + txt_job.get('1.0', 'end-1c') + '\nHere is my resume: ' +
                     txt_res.get('1.0', 'end-1c'))
    txt_paste.pack(expand=True, fill='both')


def generate_cover():
    cov = tk.Toplevel(window)
    cov.geometry("750x250")
    cov.title("Resume Text")
    txt_paste = tk.Text(cov)
    txt_paste.insert(1.0, 'Please write a personalized cover letter for this ' + entry_job.get() + ' role at ' +
                     entry_comp.get() + '.\nHere is the job description: ' + txt_job.get('1.0', 'end-1c') +
                     '\nHere is my resume: ' + txt_res.get('1.0', 'end-1c'))
    txt_paste.pack(expand=True, fill='both')


def save_resume():
    f = open('saved_resume.txt', 'w+', encoding="utf-8")
    f.write(txt_res.get('1.0', 'end-1c'))
    f.close()


def load_resume():
    txt_res.delete(1.0, 'end-1c')
    f = open('saved_resume.txt', 'r', encoding="utf-8")
    txt_res.insert(1.0, f.read())
    f.close()


window = tk.Tk()
window.title("ChatGPT Text Generator")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.columnconfigure(2, minsize=800, weight=1)

frm_btn = tk.Frame(window, relief=tk.RAISED, padx=10, pady=10)
frm_res = tk.Frame(window, relief=tk.RAISED, pady=10)
frm_job = tk.Frame(window, relief=tk.RAISED, pady=10)
txt_res = tk.Text(frm_res)
lbl_res = tk.Label(frm_res, text='Resume')
txt_job = tk.Text(frm_job)
lbl_job = tk.Label(frm_job, text='Job Description')
entry_job = tk.Entry(frm_btn)
lbl_job_name = tk.Label(frm_btn, text='Job Title: ')
entry_comp = tk.Entry(frm_btn)
lbl_comp = tk.Label(frm_btn, text='Company Name: ')
btn_gen_res = tk.Button(frm_btn, text="Generate Resume", command=generate_resume)
btn_gen_cov = tk.Button(frm_btn, text="Generate Cover Letter", command=generate_cover)
btn_sav_res = tk.Button(frm_btn, text="Save Resume", command=save_resume)
btn_load_res = tk.Button(frm_btn, text="Load Resume", command=load_resume)
btn_clr = tk.Button(frm_btn, text="Clear")

lbl_job_name.grid(row=0, column=0, stick="ew", padx=5, pady=5)
lbl_comp.grid(row=2, column=0, stick="ew", padx=5, pady=5)
entry_job.grid(row=1, column=0, stick="ew", padx=5, pady=5)
entry_comp.grid(row=3, column=0, stick="ew", padx=5, pady=5)
btn_gen_res.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_gen_cov.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
btn_sav_res.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
btn_load_res.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
btn_clr.grid(row=8, column=0, sticky="ew", padx=5)

lbl_res.pack()
txt_res.pack(expand=True, fill='both')

lbl_job.pack()
txt_job.pack(expand=True, fill='both')

frm_btn.grid(row=0, column=0, sticky="ns")
frm_job.grid(row=0, column=1, sticky='ns')
frm_res.grid(row=0, column=2, sticky='ns')

window.mainloop()
