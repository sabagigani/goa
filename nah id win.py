def brainfuck_to_python(bf_code):
    python_code = [
        "memory = [0] * 30000",
        "ptr = 0",
        "def debug_memory():",
        "    print(f'ptr: {ptr}, memory: {memory[:10]}')"
    ]
    bf_to_py = {
        '>': 'ptr += 1',
        '<': 'ptr -= 1',
        '+': 'memory[ptr] += 1',
        '-': 'memory[ptr] -= 1',
        '.': 'print(chr(memory[ptr]), end="")',
        ',': 'memory[ptr] = ord(input()[0])',
        '[': 'while memory[ptr] != 0:\n    debug_memory()',
        ']': '    debug_memory()'  # Added debug_memory() to trace the exit condition
    }
    indent_level = 0
    for command in bf_code:
        if command in bf_to_py:
            if command == ']':
                indent_level -= 1
            code_line = '    ' * indent_level + bf_to_py[command]
            python_code.append(code_line)
            if command == '[':
                indent_level += 1
    return '\n'.join(python_code)


bf_code = "++[>++<-]>."


transpiled_code = brainfuck_to_python(bf_code)
print("Transpiled Python Code:\n", transpiled_code)


try:
    exec(transpiled_code)
except Exception as e:
    print("Error during execution:", e) 