with open("stocks.csv","r") as f, open("stocks_out.csv","w") as f_out:
    f_out.write("Company Name,PE Ratio,PB Ratio\n")
    next(f)
    for line in f:
        tokens = line.strip().split(",")
        #print(tokens)
        company = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price / eps,2)
        pb = round(price / book, 2)
        f_out.write(f"{company},{pe},{pb}\n")
