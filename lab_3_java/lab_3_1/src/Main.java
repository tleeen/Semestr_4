class NewThread1 implements Runnable {
    Main main;
    NewThread1(Main main) {
        this.main = main;
    }
    public void run() {
            do {
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                main.one();
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            } while(true);
    }
}

class NewThread2 implements Runnable {
    Main main;
    NewThread2(Main main) {
        this.main = main;
    }

    public void run() {
        do {
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            main.two();
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        } while(true);
    }
}

public class Main{
    private int c = 1;
    public synchronized void one()
    {
        while (c == 1){
            try {
                wait();
            } catch (InterruptedException ignored) {
            }
    }
        c--;
        System.out.println("Поток 2");
        notify();
    }
    public synchronized void two()
    {
        while (c == 2){
            try {
                wait();
            } catch (InterruptedException ignored) {
            }
        }
        c++;
        System.out.println("Поток 1");
        notify();
    }
}

class ThreadDemo {
    public synchronized static void main(String[] args){
        Main main = new Main();
        NewThread1 newThread1 = new NewThread1(main);
        NewThread2 newThread2 = new NewThread2(main);
        new Thread(newThread1).start();
        new Thread(newThread2).start();
    }
}