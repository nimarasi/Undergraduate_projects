library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity fullsubtractor is
Port ( 	a : in STD_LOGIC;
		b : in STD_LOGIC;
		bin : in STD_LOGIC;
		diff : out STD_LOGIC;
		bout : out STD_LOGIC);
end fullsubtractor;
architecture Behavioral of fullsubtractor is
begin
diff <= a xor b xor bin;
bout <= ((not a)and b)or((not a)and bin)or(b and bin); 
end Behavioral;

