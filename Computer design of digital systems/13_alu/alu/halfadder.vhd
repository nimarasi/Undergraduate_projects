library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity halfadder is
Port( 	a,b : in std_logic;
		s : out STD_LOGIC;
		cout : out STD_LOGIC);
end halfadder;

architecture Behavioral of halfadder is
begin
s <= a xor b;
cout <= a and b;
end Behavioral;

