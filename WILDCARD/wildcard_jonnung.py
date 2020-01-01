def match(pattern, filename):
    index = 0

    while True:
        if index == len(pattern) and index == len(filename):
            return True

        if index == len(pattern) and len(filename) > 0:
            return False

        if pattern[index] != "*":
            if pattern[index] == "?" or pattern[index] == filename[index]:
                index += 1
                continue
            else:
                return False
        else:
            if index == len(filename):
                return True
            
            if pattern[index + 1] == "*":
                index += 1
                continue

            for right in range(len(filename[index:])):
                next_pattern = pattern[index + 1:]

                if not next_pattern:
                    return True

                temp_filename = filename[index + right:]
                if match(next_pattern, temp_filename):
                    return True
        
        return False

if __name__ == "__main__":
    import sys

    rl = lambda: sys.stdin.readline()
    c = int(rl())
    for _ in range(c):
        w = str(rl()).strip()
        n = int(rl())
        matched = []
        for _ in range(n):
            filename = str(rl()).strip()
            if match(w, filename):
                matched.append(filename)
        for result in sorted(matched):
            print(result)

        