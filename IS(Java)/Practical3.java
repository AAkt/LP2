package Practical;
	import javax.crypto.Cipher;
	import javax.crypto.KeyGenerator;
	import javax.crypto.SecretKey;
	import java.util.Base64;
	public class Practical3 {
	Cipher ecipher;
	Cipher dcipher;
	Practical3(SecretKey key) throws Exception {
	ecipher = Cipher.getInstance("DES");
	dcipher = Cipher.getInstance("DES");
	ecipher.init(Cipher.ENCRYPT_MODE, key);
	dcipher.init(Cipher.DECRYPT_MODE, key);
	}
	public String encrypt(String str) throws Exception {
	byte[] utf8 = str.getBytes("UTF8");
	byte[] enc = ecipher.doFinal(utf8);
	return Base64.getEncoder().encodeToString(enc);
	}
	public String decrypt(String str) throws Exception {
	byte[] dec = Base64.getDecoder().decode(str);
	byte[] utf8 = dcipher.doFinal(dec);
	return new String(utf8, "UTF8");
	}
	public static void main(String[] argv) throws Exception {
	final String secretText = "www.knowledgefactory.net";
	System.out.println("SecretText: " + secretText);
	SecretKey key = KeyGenerator.getInstance("DES").generateKey();
	Practical3 encrypter = new Practical3(key);
	String encrypted = encrypter.encrypt(secretText);
	System.out.println("Encrypted Value: " + encrypted);
	String decrypted = encrypter.decrypt(encrypted);
	System.out.println("Decrypted: " + decrypted);
	}

	}

