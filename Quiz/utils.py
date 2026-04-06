def get_int(prompt, min_v, max_v):
    while True:
        try: #에러 대비
            raw = input(prompt).strip() #입력 받기
            #빈칸 확인
            if not raw:
                print("입력 필요")
                continue
            # 문자열 -> 정수
            val = int(raw)
            # 범위 검사
            if not (min_v <= val <= max_v):
                print(f"{min_v}~{max_v} 범위 입력")
                continue
            
            return val
        # 숫자가 아닐 경우
        except ValueError:
            print("숫자만 입력")
        #사용자가 Ctrl + c를 누르거나 Ctul + d를 누르면 출력
        except (KeyboardInterrupt, EOFError):
            print("\n안전 종료 중...")
            raise