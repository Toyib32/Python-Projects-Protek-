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
public class bangunRuangMain {
    public static void main (String [] args){
        Bola bola = new Bola();
        
        bola.r = 10;
        bola.hitungVolumeBola();
        bola.hitungSelimutBola();
        
        System.out.println("");
        System.out.println("---------------------------------");
        System.out.println("");
        
        Tabung tabung = new Tabung();

        tabung.r = 20;
        tabung.t = 10;
        tabung.hitungVolumeTabung();
        tabung.hitungLuasTabung();
        
        System.out.println("");
        System.out.println("----------------------------------");
        System.out.println("");
        
        Kerucut kerucut = new Kerucut();
        kerucut.r = 10;
        kerucut.s = 30;
        kerucut.t = 20;
        kerucut.hitungVolumeKerucut();
        kerucut.hitungLuasSelimutKerucut();
    }
}
