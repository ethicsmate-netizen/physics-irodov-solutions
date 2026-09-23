import sys
sys.stdout.reconfigure(encoding='utf-8')
from part5_ch5_2a import CH5_2A_CURATED

print('Loaded CH5_2A_CURATED successfully!')
print('Count:', len(CH5_2A_CURATED))
print('Range:', CH5_2A_CURATED[0]['id'], 'to', CH5_2A_CURATED[-1]['id'])
for p in CH5_2A_CURATED:
    assert len(p['hints']) >= 3, f"{p['id']} has < 3 hints"
    assert p['answer'], f"{p['id']} has empty answer"
    assert p['solution'], f"{p['id']} has empty solution"
print('All assertions passed for CH5_2A_CURATED!')
