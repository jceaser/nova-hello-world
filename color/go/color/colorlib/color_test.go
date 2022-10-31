package colorlib
     
import "testing"
import "fmt"


func CompColorTest(t *testing.T, given [3]byte, expected [3]byte, msg string) {
    actual := FindCompliment(given)
    if expected != actual {
      t.Error(fmt.Sprintf ("%v != %v - %s", expected, actual, msg))
    }
}


func TestComplimentColor(t *testing.T) {
    CompColorTest(t, [3]byte{0,0,0}, [3]byte{255,255,255}, "Black")
    CompColorTest(t, [3]byte{0,0,255}, [3]byte{255,255,0}, "Blue")
    CompColorTest(t, [3]byte{0,255,0}, [3]byte{255,0,255}, "Green")
    CompColorTest(t, [3]byte{0,255,255}, [3]byte{255,0,0}, "Green-Blue")
    CompColorTest(t, [3]byte{255,0,0}, [3]byte{0,255,255}, "Red")
    CompColorTest(t, [3]byte{255,0,255}, [3]byte{0,255,0}, "Red-Blue")
    CompColorTest(t, [3]byte{255,255,0}, [3]byte{0,0,255}, "Red-Green")
    CompColorTest(t, [3]byte{255,255,255}, [3]byte{0,0,0}, "White")
    
    CompColorTest(t, [3]byte{127,127,127}, [3]byte{128,128,128}, "Mid point")
}