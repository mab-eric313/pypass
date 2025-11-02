import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="PyPass")
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Jalankan dalam mode GUI"
    )
    parser.add_argument(
        "--test-gui",
        action="store_true"
    )
    args = parser.parse_args()

    if args.gui:
        from app.ui.gui import GuiApp
        GuiApp().run()
    else:
        from app.ui.cli import CliApp
        CliApp().run()
