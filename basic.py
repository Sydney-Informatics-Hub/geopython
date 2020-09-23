from multiprocessing import Pool

def addit(x):
        return x + 1

def main():
        print(addit(4))
        with Pool(2) as p:
                print(p.map(addit,[1,2,3]))

main()