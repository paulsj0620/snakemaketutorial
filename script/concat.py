import re

# wc -w 결과 파싱용 정규식
PTRN = re.compile(r'\s*(\d+)\s[^\s]+([^\s\/]+.txt)')

# 출력용 csv 파일 오픈
with open(snakemake.output[0], 'wt') as f:
    f.write('fname, count\n')
    # snakefile에 명시된 모든 입력 파일에 대해서
    for fn in snakemake.input:
        # 파싱하고 출력
        line = open(fn, 'rt').read()
        cnt, fn = PTRN.search(line).groups()
        f.write('{}, {}\n'.format(fn, cnt))
