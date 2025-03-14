# กำหนดทิศทาง
up = (1, 0)  # ขึ้นบน
right = (0, 1)  # ไปทางขวา 
down = (-1, 0)  # เดินลง
left = (0, -1)  # ไปทางซ้าย
up_left = (-1, -1) # ทแยงมุมบนซ้าย
up_right = (-1, 1) # ทแยงมุมบนขวา
down_left = (1, -1) # ทแยงมุมล่างซ้าย
down_right = (1, 1) # ทแยงมุมล่างขวา

def clean_board(board):
    a = board.splitlines()  # แยกบรรทัดของกระดาน
    i = 0  # เริ่มต้นที่บรรทัดแรก
    while i < len(a):
        j = 0  # เริ่มต้นที่ตำแหน่งแรกของแต่ละบรรทัด
        new_row = ""  # สำหรับเก็บผลลัพธ์ของแต่ละบรรทัด
        while j < len(a[i]):
            if a[i][j] not in ['P', 'R', 'Q', 'B', 'K']:  # ถ้าตัวอักษรไม่ใช่หมาก
                new_row += '.'  # เปลี่ยนเป็น '.'
            else:
                new_row += a[i][j]  # ถ้าเป็นหมากไม่ต้องเปลี่ยน
            j += 1
        a[i] = new_row  # อัปเดตบรรทัดใหม่
        i += 1  # ไปที่บรรทัดถัดไป
    return "\n".join(a)  # รวมบรรทัดกลับมาเป็น string
# ฟังก์ชันตรวจสอบการคุกคามจาก Pawn
def check_Pawn(board, x, y): 
    distance = [down_right, down_left]  # ความสามารถ P
    start_check = 0
    while start_check < len(distance):
        dx, dy = distance[start_check]  # เริ่มต้นเช็ค distance
        nx, ny = x + dx, y + dy  # ทำให้สามารถเช็คตำแหน่งถัดไปได้
        if 0 <= nx < len(board) and 0 <= ny < len(board[nx]):  # ตรวจสอบไม่ให้ข้อมูลเกินขอบเขตของกระดาน
            if board[nx][ny] == 'P':  # ตรวจสอบหา P
                return True  # พบ P กำลังเช็ค
        start_check += 1  # ตรวจสอบว่า R กิน K ได้ไงจุดไหน
    return False  # ไม่เจอ P จะกิน

# ฟังก์ชันสำหรับตรวจสอบการจับของ Rook หรือ Queen
def check_rook_or_queen(board, name_mark, x, y):
    distance = [down, up, left, right]  #ความสามารถ R  Q
    start_check  = 0
    while start_check  < len(distance):
        dx, dy = distance[start_check ]
        nx, ny = x, y
        while 0 <= nx < len(board) and 0 <= ny < len(board[nx]):
            nx += dx
            ny += dy
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[nx]):
                break
            if board[nx][ny] != '.':
                if board[nx][ny] == name_mark:
                    return True
                break
        start_check += 1
    return False

# ฟังก์ชันสำหรับตรวจสอบการจับของ Bishop หรือ Queen
def check_bishop_or_queen(board, name_mark, x, y):
    distance = [up_left, up_right, down_left, down_right]  # ความสามารถของ Q , B
    start_check = 0
    while start_check < len(distance):
        dx, dy = distance[start_check]
        nx, ny = x, y
        while 0 <= nx < len(board) and 0 <= ny < len(board[nx]):
            nx += dx
            ny += dy
            if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[nx]):
                break
            if board[nx][ny] != '.':
                if board[nx][ny] == name_mark:  # ตรวจสอบว่าตรงตำแหน่งกับที่ตัวหมากอยู่ไหม
                    return True
                break
        start_check += 1
    return False
# ฟังก์ชันหลักตรวจสอบ Checkmate
def checkmate(board):
    a = board.splitlines()  # แยกบรรทัดของกระดาน

    # ค้นหาตำแหน่งของ King
    king_position = None
    row_index = 0
    while row_index < len(a):
        if 'K' in a[row_index]:
            col_index = a[row_index].index('K')
            if king_position:  # ถ้ามี K แล้ว
                print("Fail")  # หากพบ King มากกว่า 1 ตัว
                return
            king_position = (row_index, col_index)
        row_index += 1

    if not king_position:
        print("Error: No King found on the board.")
        return
    
    king_x, king_y = king_position  # ตำแหน่งของ King
    
    # ตรวจสอบการคุกคามจากทุกหมาก
    if (check_rook_or_queen(a, 'R', king_x, king_y) or
        check_rook_or_queen(a, 'Q', king_x, king_y) or
        check_bishop_or_queen(a, 'B', king_x, king_y) or
        check_bishop_or_queen(a, 'Q', king_x, king_y) or
        check_Pawn(a, king_x, king_y)): 
        print("Success")
    else:
        print("Fail")