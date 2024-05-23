#include <iostream>
#include <vector>

using namespace std;

const int CACHE_SIZE = 32768; // 32KB
const int BLOCK_SIZE = 8;     // 8B
const int WIDTH = 640;
const int HEIGHT = 480;
const int PIXEL_SIZE = 4;     // 4B

int main() {
    int numBlocks = CACHE_SIZE / BLOCK_SIZE;
    
    // Pamięć podręczna
    vector<int> cache(numBlocks, -1);
    
    int hits = 0, misses = 0;
    
    for (int j = 639; j >= 0; j--) {
        for (int i = 479; i >= 0; i--) {
            int address = ((i * WIDTH) + j) * PIXEL_SIZE;
            
            for (int k = 0; k < PIXEL_SIZE; k++) {
                int byteAddress = address + k;
                int blockIndex = (byteAddress / BLOCK_SIZE) % numBlocks;
                int tag = byteAddress / (BLOCK_SIZE * numBlocks);
                
                if (cache[blockIndex] == tag) {
                    hits++;
                } else {
                    misses++;
                    cache[blockIndex] = tag;
                }
            }
        }
    }
    
    double hitRate = static_cast<double>(hits) / (hits + misses);
    cout << "Trafienia: " << hits << ", nietrafienia: " << misses << endl;
    cout << "Współczynnik trafień: " << hitRate << endl;
    
    return 0;
}
