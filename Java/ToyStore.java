package Java;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class ToyStore {
    private List<Toy> toys = new ArrayList<>();
    private String prizeFileName = "prize_toys.txt";

    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public void updateToyWeight(int toyId, double weight) {
        for (Toy toy : toys) {
            if (toy.getId() == toyId) {
                toy.setWeight(weight);
                return;
            }
        }
        System.err.println("Игрушка с ID " + toyId + " не найдена.");
    }

    public Toy drawPrizeToy() {
        if (toys.isEmpty()) {
            System.err.println("Нет доступных игрушек для розыгрыша.");
            return null;
        }

        double totalWeight = toys.stream().mapToDouble(Toy::getWeight).sum();
        Random random = new Random();
        double randomValue = random.nextDouble();

        double cumulativeWeight = 0;
        for (Toy toy : toys) {
            cumulativeWeight += toy.getWeight() / totalWeight;
            if (randomValue <= cumulativeWeight && toy.getQuantity() > 0) {
                Toy prizeToy = new Toy(toy.getId(), toy.getName(), 1, toy.getWeight());
                toy.reduceQuantity();
                return prizeToy;
            }
        }

        System.err.println("Не удалось определить призовую игрушку.");
        return null;
    }

    public void savePrizeToyToFile(Toy prizeToy) {
        if (prizeToy == null) {
            System.err.println("Нечего сохранять.");
            return;
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(prizeFileName, true))) {
            writer.write(prizeToy.getName());
            writer.newLine();
            System.out.println("Призовая игрушка сохранена в файл: " + prizeFileName);
        } catch (IOException e) {
            System.err.println("Ошибка при записи данных в файл: " + e.getMessage());
        }
    }
}
