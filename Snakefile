rule count:
    """word counting in files"""
    input:
        "data/{filename}.txt"
    output:
        "output/wc_{filename}.txt"
    shell:
        "wc -w {input} > {output}"

#rule concat:
#    """merging word text files"""
#    input:
#        "output/wc_A.txt",
#        "output/wc_B.txt",
#        "output/wc_C.txt"
#    output:
#        "temp/wc_all.csv"
#    script:
#        "script/concat.py"
