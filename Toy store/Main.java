//Метод добавление новых игрушек и возможность изменения веса (частоты выпадения игрушки)
//Возможность организовать розыгрыш игрушек.
// Например, следующим образом:
// С помощью метода выбора призовой игрушки – мы получаем эту призовую игрушку и записываем в список\массив.
// Это список призовых игрушек, которые ожидают выдачи.
// Еще у нас должен быть метод – получения призовой игрушки.
// После его вызова – мы удаляем из списка\массива первую игрушку и сдвигаем массив. А эту игрушку записываем в текстовый файл.
// Не забываем уменьшить количество игрушек
// К написанию программы можно подойти более творчески и делать так, как Вы поняли задание. Немного менять и отходить от примера выше.

//Приложение должно запускаться, записывать значения в файл

import java.util.Queue;

public class Main {
    public static void main(String[] args) throws InputSexException {
            Queue<String> toy = ToyStore.getRandomToy();
            String x = ToyStore.yourSex();
            ToyStore.getYourToy(toy, x);

    }
}

