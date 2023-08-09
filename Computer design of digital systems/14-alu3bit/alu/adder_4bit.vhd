library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity adder_4bit is
Port ( 	a : in STD_LOGIC_VECTOR (2 downto 0);
		b : in STD_LOGIC_VECTOR (2 downto 0);
		cin : in STD_LOGIC;
		sum : out STD_LOGIC_VECTOR (2 downto 0);
		cout : out STD_LOGIC);
end adder_4bit;

architecture Behavioral of adder_4bit is 

component fulladder 
port( 	a : in STD_LOGIC; 
		b : in STD_LOGIC; 
		cin : in STD_LOGIC; 
		s : out STD_LOGIC; 
		cout : out STD_LOGIC); 
end component; 

signal c1,c2,c3:std_logic; 
begin
	fa1:fulladder port map(a(0),b(0),cin,sum(0),c1); 
	fa2:fulladder port map(a(1),b(1),c1,sum(1),c2); 
	fa4:fulladder port map(a(2),b(2),c3,sum(2),cout); 
end Behavioral;

