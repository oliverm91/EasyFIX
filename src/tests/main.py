from time import time

from EasyFIX.parser import create_fix_message
from EasyFIX.definitions.market_data.tags import MDTags

def clean_lines(raw_lines: list[bytes]) ->  list[bytes]:
    target_sequence = b'\x0135=X'
    return [raw_line[raw_line.find(b'8=FIX.4.4'):][:-2] + b'\x01' for raw_line in raw_lines if target_sequence in raw_line]

def get_messages() -> list[bytes]:
    with open('tests/mdbcsrf_tr-fix-messages.log', 'rb') as f:
        log_lines = f.readlines()
        cleaned_lines = clean_lines(log_lines)
        t0 = time()
        for cleaned_line in cleaned_lines:
            fm = create_fix_message(cleaned_line)
        t1 = time()
        total_t = round(t1-t0,4)
        n = len(cleaned_lines)
        print(f'{n} MD_INCREMENTAL_REFRESH messages parsed in {total_t}: {round(n/total_t, 1)} messages/second, {round(1000*total_t/n,4)} ms/message.')
            
        return cleaned_lines
    
get_messages()