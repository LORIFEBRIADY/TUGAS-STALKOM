class Printer:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Tidak ada Antrian yang akan dicetak"
        
    def is_full(self):
        return len(self.items)== self.max_size
        
    def peek(self):
        if not self.is_empty():
                return self.items[0]
        else:
            return "Printer Siap digunakan"
    
    def display(self):
        print("Lihat Daftar Cetak : ", self.items)


if __name__ == "__main__":
    printer_queue = Printer()
    while True:
        print("\n=====LORI PRINTER=====")
        print("1. Tambahkan file yang di cetak")
        print("2. Cetak file berikutnya")
        print("3. Lihat semua file antrian cetak")
        print("5. Selesai Mencetak")
        
        pilihan = input("Masukkan pilihan Anda (1-4) : ")

        if pilihan == "1":
            file = input("Masukkan nama file yang ingin dicetak : ")
            printer_queue.enqueue(file)
            print(f"'{file}' telah ditambahkan ke daftar cetak.")
        elif pilihan == "2":
            if printer_queue.is_empty():
                print("Tidak ada file dalam antrian untuk dicetak.")
            else:
                file_dicetak = printer_queue.dequeue()
                print(f"Sedang mencetak file : {file_dicetak}")
        elif pilihan == "3":
             printer_queue.display()
             print("Daftar antrian file yang akan dicetak")
        elif pilihan == "4":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
