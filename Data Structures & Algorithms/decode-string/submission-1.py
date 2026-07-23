class Solution:
    def decodeString(self, s: str) -> str:
        stack = []          # holds (previous_string, repeat_count)
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # pause current progress, remember it, start fresh
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == ']':
                prev_string, num = stack.pop()
                current_string = prev_string + current_string * num
            else:  # letter
                current_string += char

        return current_string