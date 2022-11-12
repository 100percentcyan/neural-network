from saved_epochs import EPOCHS_ARRAY

def main():
          EPOCHS_ARRAY.array = [f"EPOCHS:{20}"]
          EPOCHS_ARRAY.save_epochs("EPOCHS.txt")
          input("")

if __name__ == "__main__":
          main()

