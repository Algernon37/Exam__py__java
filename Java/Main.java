package Java;


public class Main {
    public static void main(String[] args) {
        ToyStore toyStore = new ToyStore();

        toyStore.addToy(new Toy(1, "Мяч", 10, 30));
        toyStore.addToy(new Toy(2, "Кукла", 15, 20));
        toyStore.addToy(new Toy(3, "Кубики", 20, 10));

        toyStore.updateToyWeight(1, 40);

        Toy prizeToy = toyStore.drawPrizeToy();

        if (prizeToy != null) {
            System.out.println("Выиграли игрушку: " + prizeToy.getName());
            toyStore.savePrizeToyToFile(prizeToy);
        } else {
            System.out.println("Нет доступных призовых игрушек.");
        }
    }
}