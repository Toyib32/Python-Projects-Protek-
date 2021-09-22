/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bangunruang;

/**
 *
 * @author ASUS
 */
public class Tabung {
    //atribut 
    public int r;
    public int t;
    
    //method 
    public void hitungVolumeTabung(){
        double vol = (3.14 * r * r) * t;
        System.out.println("Volume Tabung adalah : " + vol);
    }
    
    public void hitungLuasTabung(){
        double alasTabung = 3.14 * r * t;
        double selimut = 2 * 3.14 * r * t;
        
        double totalSelimut = alasTabung + selimut;
        System.out.println("Luas selimut tabung adalah : " + totalSelimut);
    }
}
