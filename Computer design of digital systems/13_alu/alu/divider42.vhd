library ieee;
use ieee.std_logic_1164.all;
Use ieee.std_logic_unsigned.all;
Use ieee.std_logic_unsigned.all;

Entity div84 is
	port(
	numerator : in std_logic_vector (7 downto 0);
	denominator : in std_logic_vector (3 downto 0);
	quotient : out std_logic_vector (7 downto 0);
	remainder : out std_logic_vector (3 downto 0));

End div84;

Architecture div84 of div84 is
Procedure div4(
	number : in std_logic_vector (7 downto 0);
	denom : in std_logic_vector (3 downto 0);
	quotient : out std_logic_vector (3 downto 0);
	remainder : out std_logic_vector (3 downto 0 )) is
	Variable d,n1 : std_logic_vector (4 downto 0);
	Variable n2 : std_logic_vector (3 downto 0);
Begin
	d := '0' & denom;
	n2 := number(3 downto 0);
	n1 := '0' & number(7 downto 4);
	for i in 0 to 3 loop
			n1 := n1 (3 downto 0 ) & n2(3);
			n2 := n2 (2 downto 0 ) & '0';
		if n1 >= d then
			n1 := n1 - d;
			n2(0) := '1';
		end if;
End loop;
Quotient := n2;
Remainder := n1 (3 downto 0);
End procedure;

Begin
	process(numerator,denominator)
	variable remH,remL,qoutH,qoutL : std_logic_vector (3 downto 0);
	begin
		div4("0000" & numerator(7 downto 4), denominator,qoutH,remH);
		div4(remH & numerator(3 downto 0), denominator,qoutL,remL);
		quotient(7 downto 4 ) <= qoutH;
		quotient(3 downto 0 ) <= qoutL;
		remainder <= remL;
	end process;
End div84;
