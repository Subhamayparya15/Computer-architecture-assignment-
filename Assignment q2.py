PAGE_SIZE = 1024
page_table = {
    0: 5,
    1: 9,
    2: 3,
    3: 7
}

virtual_addresses = [100, 1200, 2500, 3500]

for va in virtual_addresses:
    page_number = va // PAGE_SIZE
    offset = va % PAGE_SIZE

    print("\nVirtual Address:", va)
    print("Page Number:", page_number)
    print("Offset:", offset)

    if page_number in page_table:
        frame_number = page_table[page_number]
        physical_address = frame_number * PAGE_SIZE + offset

        print("Frame Number:", frame_number)
        print("Physical Address:", physical_address)
    else:
        print("Page not found in page table")
      
