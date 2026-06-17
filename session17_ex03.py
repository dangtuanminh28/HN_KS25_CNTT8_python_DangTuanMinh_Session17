import itertools

teams_list = ['T1', 'GEN.G', 'WBG', 'BLG']
matches_list = ['T1 vs GEN.G', 'T1 vs WBG', 'T1 vs BLG', 'GEN.G vs WBG', 'GEN.G vs BLG', 'WBG vs BLG']

def add_team(teams_list):
    raw_input = input("Nhập danh sách các đội tuyển (cách nhau bởi dấu phẩy): ").strip()
    if raw_input == "":
        print("Bạn chưa nhập dữ liệu!")
        return teams_list
        
    raw_teams = raw_input.split(',')
    new_added_teams = []
    
    for team in raw_teams:
        cleaned_team = team.strip().upper()
        if cleaned_team != "": 
            teams_list.append(cleaned_team)
            new_added_teams.append(cleaned_team)
            
    print(f"Đã ghi nhận {len(new_added_teams)} đội: {new_added_teams}")
    return teams_list


def add_schedule(teams_list):
    if len(teams_list) < 2:
        print("Cần tối thiểu 2 đội bóng để tạo lịch thi đấu!")
        return []
        
    local_matches = []
    all_combinations = itertools.combinations(teams_list, 2)
    
    for match in all_combinations:
        match_string = f"{match[0]} vs {match[1]}"
        local_matches.append(match_string)
        
    print("--- LỊCH THI ĐẤU VÒNG BẢNG ---")
    for index, match_name in enumerate(local_matches, start=1):
        print(f"{index}. {match_name}")
        
    print(f"Tổng số trận đấu: {len(local_matches)} trận.")
    return local_matches


def add_match_ids(matches_list):
    if not matches_list:
        print("Chưa có lịch thi đấu!")
        return []
        
    match_ids_list = []
    print("--- MÃ TRẬN ĐẤU (MATCH ID) ---")
    
    for index, match in enumerate(matches_list, start=1):
        teams = match.split(' vs ')
        team_a = teams[0]
        team_b = teams[1]
        
        code_a = f"{team_a[0:3]:X<3}"
        code_b = f"{team_b[0:3]:X<3}"
        
        match_number = f"{index:02d}"
        match_id = f"M{match_number}-{code_a}-{code_b}"
        
        match_ids_list.append(match_id)
        print(f"Trận {index} ({match:<13}) -> ID: {match_id}")
    return match_ids_list

while True:
    print("""
============= ESPORTS MATCHMAKER =============
1. Nhập danh sách Đội tuyển
2. Tạo lịch thi đấu (Combinations)
3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)
4. Đóng hệ thống
==============================================
""")
    choice = input("Chọn chức năng (1-4): ").strip()
    
    if choice == '1':
        teams_list = add_team(teams_list)
    elif choice == '2':
        matches_list = add_schedule(teams_list)
    elif choice == '3':
        match_ids = add_match_ids(matches_list)
    elif choice == '4':
        print("Thoát chương trình. Tạm biệt!")
        break
    else:
        print("Vui lòng nhập lại số hợp lệ (1-4)!")