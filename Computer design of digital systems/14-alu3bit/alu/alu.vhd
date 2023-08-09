library IEEE;
use IEEE.STD_LOGIC_1164.ALL; 

entity ALU is
Port ( 	a : in STD_LOGIC_VECTOR (2 downto 0); 
		b : in STD_LOGIC_VECTOR (2 downto 0); 
		c: in std_logic; 
		sel : in STD_LOGIC_VECTOR (1 downto 0); 
		result : out STD_LOGIC_VECTOR (5 downto 0)); 
end ALU; 

architecture Behavioral of ALU is 

component comparator_3bit 
port( 	a : in std_logic_vector(2 downto 0); 
		b : in std_logic_vector(2 downto 0); 
		less : out std_logic; 
		equal : out std_logic; 
		greater : out std_logic); 
end component; 
 
component multiplier_4bit 
Port ( 	a : in STD_LOGIC_VECTOR (2 downto 0); 
		b : in STD_LOGIC_VECTOR (2 downto 0);  
		p : out STD_LOGIC_VECTOR (5 downto 0)); 
end component;
 
component subtractor_4bit 
Port ( 	a : in STD_LOGIC_VECTOR (2 downto 0); 
		b : in STD_LOGIC_VECTOR (2 downto 0); 
		bin : in STD_LOGIC; 
		diff : out STD_LOGIC_VECTOR (2 downto 0); 
		bout : out STD_LOGIC); 
end component; 
 
component adder_4bit is 
Port ( 	a : in STD_LOGIC_VECTOR (2 downto 0); 
		b : in STD_LOGIC_VECTOR (2 downto 0); 
		cin : in STD_LOGIC; 
		sum : out STD_LOGIC_VECTOR (2 downto 0); 
		cout : out STD_LOGIC); 
end component;
signal t_multi,t_sub,t_adder:std_logic_vector(5 downto 0);

begin
	alu1: adder_4bit port map(a=>a,b=>b,cin=>c,sum=>t_adder(2 downto 0),cout=>t_adder(3));
	alu2: subtractor_4bit port map(a=>a,b=>b,bin=>c,diff=>t_sub(2 downto 0),bout=>t_sub(3));
	alu3: multiplier_4bit port map(a=>a,b=>b,p=>t_multi);
	
process(sel,t_multi,t_sub,t_adder)
begin
case sel is
when "00"=>
	result<=t_adder; when "01"=>
	result<=t_sub; when "10"=>
	result<=t_multi; when "11"=>
	result<="000000";
end case;
end process;
end Behavioral;

