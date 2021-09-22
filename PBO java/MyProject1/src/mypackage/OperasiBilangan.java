package mypackage;

public class OperasiBilangan {
    
    // atribut
    public int bilPertama;
    public int bilKedua;
    
    // methods
    public void hitungPenjumlahan(){
        int hasil = bilPertama + bilKedua;
        System.out.println("Hasil penjumlahannya: " + hasil);
    }
    
    public void hitungPengurangan(){
        int hasil = bilPertama - bilKedua;
        System.out.println("Hasil pengurangannya: " + hasil);
    }
    
    //method tambahan
        public void hitungPerkalian(){
        int hasil = bilPertama * bilKedua;
        System.out.println("Hasil perkaliannya: "+ hasil);
    }
    
    public void hitungPembagian(){
        double bilPertamaDouble = bilPertama;
        double bilKeduaDouble = bilKedua;
        
        double hasil = bilPertamaDouble / bilKeduaDouble;
        System.out.println("Hasil pembagiannya: "+ hasil);
    }
}

