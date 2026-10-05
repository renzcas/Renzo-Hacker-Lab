import sys
from cli.commands import CLICommands

def main():
    cli = CLICommands()

    if len(sys.argv) < 2:
        print("Usage: python -m cli.main <command> [args]")
        return

    cmd = sys.argv[1]

    if cmd == "run":
        ticks = int(sys.argv[2]) if len(sys.argv) > 2 else 50
        cli.cmd_run(ticks=ticks)

    elif cmd == "save":
        path = sys.argv[2] if len(sys.argv) > 2 else "world_state.json"
        cli.cmd_save(path)

    elif cmd == "load":
        path = sys.argv[2] if len(sys.argv) > 2 else "world_state.json"
        cli.cmd_load(path)

    elif cmd == "pulse":
        cli.cmd_pulse()

    elif cmd == "organs":
        cli.cmd_organs()

    elif cmd == "ascend":
        cli.cmd_ascend()

    elif cmd == "collapse":
        cli.cmd_collapse()

    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
