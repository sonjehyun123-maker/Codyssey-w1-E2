from Quizgame import QuizGame

def main():
    game = QuizGame() #객체 생성

    try:
        game.run() 
    except (KeyboardInterrupt, EOFError): #ctrl+c 종료
        print("\n안전 종료")
        game.save()
# 이 파일이 직접 실행될 때만 main() 실행
if __name__ == "__main__":
    main()