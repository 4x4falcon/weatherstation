<?php

// user agent can be changed for different esp32 or d1 mini pro

if ($_SERVER['HTTP_USER_AGENT'] == "uP-wemosd1minipro" ) {
		//ESP talking to this site
		// add correct username, password and database below
		$servername = "localhost";
		$username = "<<<USERNAME>>>";
		$password = "<<<PASSWord>>>";
		$dbname = "<<<DataBase>>>";



		if ( !empty($_POST) ) {

			if (($_POST['t'] != -99) && ($_POST['p'] != -99) && ($_POST['h'] != -99)) {

				$conn = mysqli_connect($servername, $username, $password, $dbname);

				$sql = "";

				$sql .= "INSERT INTO weatherout (timestamp, temperatureout, pressureout, humidityout, dewout, voltage, rainfall, windspeed, winddir)
				VALUES ('" . $_POST["ti"] . "', '" . $_POST["t"] . "', '" . $_POST["p"] . "', '" . $_POST["h"] . "', '" . $_POST["d"] . "', '" .
					 $_POST["v"] . "', '" . $_POST["rf"] . "', '" . $_POST["ws"] . "', '" . $_POST["wd"] . "');";


				if (mysqli_query($conn, $sql)) {

					echo "0";

				} else {
					echo "Error: " . $sql . "<br>" . mysqli_error($conn);
				}

			mysqli_close($conn);
			} else {
				echo "1";
			}
		} else {
			echo "1";
		}

} else {
echo "Only for my ESP!\n\n" . $_SERVER['HTTP_USER_AGENT'];
}
?>

