from Quizgame import QuizGame

def main():
    game = QuizGame()

    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n안전 종료")
        game.save()

if __name__ == "__main__":
    main()