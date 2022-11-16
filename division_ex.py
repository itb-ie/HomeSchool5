try:
    deimpartit = int(input("Deimpartitul este: "))
    impartitor = int(input("Impartitorul este: "))
    rezultatul = deimpartit / impartitor
except ValueError:
    print("introdu termenii corect")
except ZeroDivisionError:
    print("impartitorul nu poate fi zero")
except:
    print("Some other error I did not see coming")
else:
    # asta se executa doar daca nu a fost nici o exceptie
    print("Rezultatul este:", rezultatul)
finally:
    # indiferent, asta se executa la final
    print("hasta la vista")
