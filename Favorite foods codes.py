def read_all():
    file = open('favorite_foods.txt', 'r')
    
    all_lines = file.read()
    
    print(all_lines)
    
    file.close()
    
def main():
    read_all()
    
main()
print('These are some of my favorite foods')