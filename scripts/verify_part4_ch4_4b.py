import sys
sys.stdout.reconfigure(encoding='utf-8')
from part4_ch4_4b import CH4_4B_CURATED

print('Loaded CH4_4B_CURATED successfully!')
print('Count:', len(CH4_4B_CURATED))
print('Range:', CH4_4B_CURATED[0]['id'], 'to', CH4_4B_CURATED[-1]['id'])
for p in CH4_4B_CURATED:
    assert len(p['hints']) >= 3, f"{p['id']} has < 3 hints"
    assert p['answer'], f"{p['id']} has empty answer"
    assert p['solution'], f"{p['id']} has empty solution"
print('All assertions passed for CH4_4B_CURATED!')
