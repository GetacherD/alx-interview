#!/usr/bin/python3
"""
Read from std in parse
"""
import sys
import asyncio


def ReadAll():
    """ read from stdin """
    data = {"200": 0, "301": 0, "400": 0, "401": 0,
            "403": 0, "404": 0, "405": 0, "500": 0}
    count = 0
    size = 0
    while True:
        try:
            line = sys.stdin.readline()
            size += int(line.split(" ")[-1][0:-1])
            if "Exit".upper() == line.rstrip().upper() or not line:
                print(f"File size: {size}")
                for key, val in data.items():
                    if val:
                        print(f"{key}: {val}")
                break
            if count == 10:
                print(f"File size: {size}")
                for key in sorted(data.keys()):
                    if data[key]:
                        print(f"{key}: {data[key]}")
                        data[key] = 0
                count = 0
            count += 1
            stat = line.split(" ")[-2]
            if stat in data.keys():
                data[str(stat)] += 1
        except KeyboardInterrupt:
            print(f"File size: {size}")
            for key, val in data.items():
                if val:
                    print(f"{key}: {val}")
            sys.exit(1)


if __name__ == "__main__":
    asyncio.run(ReadAll())
