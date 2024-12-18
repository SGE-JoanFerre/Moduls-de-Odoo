# Activitats

## Activitat 01: Llista de tasques

1. **Vista Kanban:** Afegir una nova vista en format Kanban per gestionar tasques.
2. **Vista Calendar:** Associar una data a cada tasca i crear una vista de calendari per visualitzar aquestes dates.

---

## Activitat 02: Biblioteca de còmics

1. **Gestió de socis:** Implementar un model per registrar socis amb dades bàsiques (nom, cognoms i identificador).
2. **Gestió d'exemplars:**
   - Crear un model per gestionar exemplars de còmics disponibles per a préstec.
   - Associar els exemplars amb els socis i controlar la data d'inici i final del préstec.
   - Validar que la data de préstec i de devolució siguen coherents (ni abans ni després del dia actual).

---

## Activitat 03: Gestió d’hospital

1. **Pacients:** Model per gestionar nom, cognoms i símptomes.
2. **Metges:** Model per gestionar nom, cognoms i número de col·legiat.
3. **Atencions mèdiques:**
   - Model per registrar el diagnòstic de cada atenció.
   - Relacionar múltiples metges amb múltiples pacients mitjançant aquest model.

---

## Activitat 04: Cicles formatius a un institut

1. **Cicle formatiu:** Model per representar cada cicle amb els mòduls associats.
2. **Mòdul:** Model relacionat amb els cicles, alumnes matriculats i professor assignat.
3. **Alumne:** Model relacionat amb els mòduls en què està matriculat.
4. **Professor:** Model relacionat amb els mòduls que imparteix.
5. **Seguretat:**
   - Els usuaris amb rol "Director" poden modificar els registres de tots els models.
   - Els usuaris amb rol "Professor" només poden veure en mode lectura les dades dels professors.
