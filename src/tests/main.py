def clean_lines(raw_lines: list[bytes]) ->  list[bytes]:
    target_sequence = b'\x0135=X'
    return [raw_line[raw_line.find(b'8=FIX.4.4'):][:-2] + b'\x01' for raw_line in raw_lines if target_sequence in raw_line]

def get_messages() -> list[bytes]:
    with open('tests/mdbcsrf_tr-fix-messages.log', 'rb') as f:
        log_lines = f.readlines()
        cleaned_lines = clean_lines(log_lines)
        for cleaned_line in cleaned_lines:
            cl = cleaned_line.decode().replace('\x01', '|')
            if '10141=' in cl:
                print(cl)
        return cleaned_lines
    
get_messages()