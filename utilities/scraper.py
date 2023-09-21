"""Where the final call will go to run the scraper"""

from storage import write_data

def main():
    try:
        write_data()
    except Exception as err:
        print(f'Error in running scraper: {err}')

if __name__ == '__main__':
    main()