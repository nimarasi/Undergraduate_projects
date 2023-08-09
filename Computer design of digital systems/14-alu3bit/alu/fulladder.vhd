 
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity fulladder is 
port( 	a : in STD_LOGIC; 
		b : in STD_LOGIC; 
		cin : in STD_LOGIC; 
		s : out STD_LOGIC; 
		cout : out STD_LOGIC); 
end fulladder; 

architecture Behavioral of fulladder is
component halfadder
Port( 	a,b : in std_logic;
		s : out STD_LOGIC;
		cout : out STD_LOGIC);
end component;
signal s1,c1,c2:std_logic;

begin
	ha1: halfadder port map(a,b,s1,c1);
	ha2: halfadder port map(s1,cin,s,c2);
	cout <= c1 or c2;
end Behavioral;

