#include <iostream>
#include <string>
#include <array>
#include <iterator>
#include <algorithm>
int main()
{
	std::array<int, 3> a1 {{1, 2, 3}};
	std::array<int, 3> a2 = {10, 20, 30};
	std::array<std::string, 2> a3 = { std::string("a"), "b" };

	// Print  the a2 array elements in reverse order
	std::reverse_copy(a2.begin(), a2.end(), std::ostream_iterator<int> (std::cout," "));
	std::cout << "\n";

	// print the array elements a3
	for(const auto& s: a3)
		std::cout << s << " ";
}