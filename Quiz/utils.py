def get_int(prompt, min_v, max_v):
    while True:
        try:
            raw = input(prompt).strip()

            if not raw:
                print("입력 필요")
                continue

            val = int(raw)

            if not (min_v <= val <= max_v):
                print(f"{min_v}~{max_v} 범위 입력")
                continue

            return val

        except ValueError:
            print("숫자만 입력")

        except (KeyboardInterrupt, EOFError):
            print("\n안전 종료 중...")
            raise