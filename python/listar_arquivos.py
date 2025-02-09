    # Lista com todos os arquivos pdf do diretorio de output
    pdf_files = [f for f in os.listdir(dir) if f.endswith('.pdf')]
    print(f"Arquivos pdf encontrados: {pdf_files}")
