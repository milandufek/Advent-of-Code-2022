# https://adventofcode.com/2022/day/6

example_stream = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
stream = 'mzrzqrzqrrmcmgmrggvjvcczbczccdwdcwcpwwclwwbttdntnsnllpggqhgqgzqggvjjjfqfhhbbvzvmzvvfccnznwntnptpgpcplpwwvgvzvvcgvvbcvcqqhnqqbsbdsbbbgtgvtgvtgvvrfvvjbjcbcchnhrhvvrmmwzwzmwmggjwwwwzrrmbmbmbrrdjrjfrrrmrffzgghtggwddtllhchdhsshjjwfwsfssnbbnjncczsczzvpvssljsjgsjgjcgjggspsfsfhfppsqqzlzjllblsldsldlndnhnffflwfwmwssvzzvqzzblzbbmrrfnrrqnnhfnnhphbhrrlvrlvrvcrrltrtmrrcscchdhqhfffrddzsszwwrbrfftddbwwtdtnndrrghgcgfgrglllcdcsswvwsvszsddjwdwwcvwvmvhhlqlddbhbrrnddpqpttrtctmcmjjtvjjfvvlcldltdtdqdllnrncrnrznzfnfsfnndqqbhhlnhhhsmhhfghgppflllrhhvdddvrvnrnpplwplldttswsbwwtbbvwbwnnhcczmczmczclcttwcchllmsmbbrvbbsjsswbwwbtwtgtrgtrgrnggqwgwmwrmrqmmghhtbbrppjmpppjtjtffvqvbbwsspzsstlstltrrtmtrmrzmmgqqgmmpzmpzpmmgnnrjjgrjjhgjjsccjllwzzsddznnrsrttdllcnntvnttqjjqljqqwlqlmmfdfttzzvgvtvjjwvwsvvhbhrbhbwbzbppbplphpjpzppljjnttnvnggqbqffqgqrrjwjcjllcblbqqglqgqjqrrffjqqqcvqccgrgqgrqrnqqhphccvwwsgspprmprrwdrwrdwdrwrwswbsbcctscttwvvvstvthtrhhddtppgwwqpwwzpzgzszgzvggzqqmbqqrqsrqrmmjjfggztzdzvvqdqzddrrnmmtccsstdsdrrmrnnzzpggbmbqbcbzczppbjbssfzfcfvcvlclgcglcgllvclcwwwpmwwjrrgtrtfrrnznssvvrjvrjrgjrrcsrrstrsrhrpplfljjwrwbbffdpfpzffrhhjrjdrrgpggbhhschcdcdcqcnncjcvjcvjvbvcbvbssnhhsddclcrcrjrdrtdtqdqrddddlcdcttzzlslblbqqcmmdgmmsnmnmccqmmljjncnhnchcdchddwsdssdrsscfcnffcqfqtfqqjcjrrvbrvvhsvvlqlwwsccjbbgpgzgcgbgzgccpvcpvpddqrrqfqtqrqqcjjwvwttrwwblwlrwllnsshdhqdhqqjllzlflvlgllhnllstsbbdqqpnpwpmwwzhzvzcclcvcfvcvssdcdvdpphcphcppffndfnfmfbfwwgzwwwvhwwmcwwwtmtgtvggvbggzzthzzlbzbzmmhlllvgllmfmpmbbldbdnnzzjcctvvsdvssrpsslglqggcchvcvllzhhbcczjjgllvqlvlflglwwscctfcbmdjhgwtfhjrgvvvrmdcpsrtsnvhwnnznnnmrhcnlnmjvdbqztspwbdwlttdtwlwdvqjpgqdzbnssglqczqwvfgdlbdmsbbmggjdhddzvzlqhrggvvccmcmtqdmmpqvvstmqgvntdsmjbzbwstdrmjjmzfgmczjrftwrwnfbdmlddvzdfwwztldqfvdswfdwrfcgptmmjnzngwnflzlvtwpdsvllfwqjnjjjbfcwmgrvlhdvpgprnjthlqlbtlhflzwqjwtqtdzcvqbgtjlnmwchpjrgfndrnzwctjwvwsvflmgnqmplhhwljqcshqqldcnfrdbdcbslrtbnqrvhhjrddmjbtmcjzlqcdcqbfftsmpdpnfrjjwmdpmrvjjmppbnmcbvnzbphjcjlldnpdcwsqfgpmbszvjbpzngvncbfncpmghfrsssrnbbmhnjjvgmjzwtwlpszphgwvtjzdsmvvhnrplmnrllvqvphtbbrnlwmffdmmbhvzfcnbnlbspfwbcbjwgpnbsfpfbdqbnpfcqpngfqwlwcgrzlvfqgfsbppgmfzgjdntdvzvzclbrfwpqmvgmtmppsjzjhqbgjnntdnwvwljndqbtfgrjcfnlpsgsmbdljdzqfclgwhdgndzwbcthmrgzcjbhrrltlsznbsvswtsjbhwqzwchwzbtqmnrqfrzspwrqwwqwvczmntwggltjmvwdftplrgtrltmpvvgslvhctnwwcgtblmqtnsmqdgcbvzlcbrrsstzgzrgzgtmqtvsnzqqwlfgrjbdsvpdjpgmmczddbptwvpthvdjvrpqsbbgctrpqsdnczzbttdrbflrllrnvjswslnghdqfqlnbcctwbnpvspfmrcnprpjzgwsdwlszzpdcgvzjsjtdgjnpwgtqmvsmsvzddcmfwtqjghrrrmvcjbccgrngcvvfvrrmmqmzsvhdqsfqpqnnhhpffrtblnzhwqmsgvvzvgpbczsznzlnvsgjjzqbpjmvpjzqqpzpvplwsvgtwvrhlvggrpvztvchbcwflwhwmvdslvhsgpcqhdhcpvclgmzdngsmbplzrqgwflltzgsglflhqhpnnfszvtgprqhnjlrvwfsjfpcjzbznsprtldvwjlnhqsdlfnwtlpzldfpnjpnnqfgqqrjrnszznlrjgwwlnbbznzcshtfqcprphgsldtgzzgqjvmjrtfhmgptrnqzmtfclqwgprvjptntgwhbqwhdjcfjtrmdwbslhqwgtcqwhjhhmltrlsqbvzqsjqsczvsqlsjdgmnjnpvmmwbsfnfnshmlrdgslbfrnhmdgcjgsqgwlbmlhhnfmcfnswmwgrzmpdmtrcmwgjlgrhzchmhmbjgjrfgdvplvngjnfdrscwqtnsspdszznnnjrdmvwbvnzmmddbcvsphfqsbcmfmfgrcdfjptzqfsjsmjtbswtqzvtfpwbvqsgjzftfssdmcngtgbfmrrsjtllnpsztvgbpgpcrmqsgvcjrpprhqzjwlcdjpvgrqtjcglwnvzvqtncmndzbgpgfbprpqqjfbnzhfzlfrgnfnbpjfrbtjgrgvmczthqsbfplnzvhqjmrrssnzjdhfvlngwptzzdshzhzfpzhmrcjmdvlnlqtsnlbhqgplsltgznshthcwnpzpcgjjwhjstfcdtmmnvbgqzrjpsqwlmlbjnqtrfmbrdsbdlrrwqqvzdnmzhzvrhdftzldzjrtfgzlrwczbzzzqtthdcjtqpcfdwpqlzqmrnsnhwbzhjnqjzgfdcdcrqsjfhpjcdtwnvwzzbwfgdzcmmfvdvdpjsltcrbfqczvvbjscptjsvzndgwhzfjcqljndrcqzhssnqtmjmwjrsqdpqnhwsntqnmrwhvsnvrvpvwbndpmgsnchtnzpjgshcvjgwlwdhqbqhvcwqmwllhcgvbslqvwgswvnsqvvcphbglrvlsczcscznlwzrvjptmbmrgjlhvbrlghcwjdqjlgrcbrhfmbcwgclqzllqtmshbjnhwpgsgtljbwhgcsznvslmglcnmmgjlsptgdqlbtclfbfvjpmqgwwbcvwtdhgjlpvgggjjvmltdgzjdsvtswgblgfcvdvtwrrfljtqjhdflhbtwmcdqpmdqrtjsvdhzstfnqjrzztnwslvwtvgvzfqlzfrhnthjfpvmwmdgrtzhbtwdfscdpwmwwrhgbmqrdftvjvrgzhbpqtqvvlwbmbvlszzqjwhtvwnsjcdcgdlwlrtvjsdqzngcdtpvsddsbqbhtrrpwqdhvdmnnncgccszqtbcgwbdbwrnwrhpwprslbmhrmwpmqzvssfzvrmwrmrzmhrcwvbdtvdflgmrghqngwsgrnctsnhpnmcmfmrtszttqtvvlhdjgplvgnjrtgnfgmdtvwzmzbtzvmhdvpcjqvgpsmdcfrbmqbrlsnccldrfdldqfnsfzznqtvsgwbljgrvbdmggdmhvvdzjfllzwzpddcnvrfggsddqmczfnnfvrwsmvfctctjqdrhvlntflccqgzg'


def find_marker(stream: str, seq_len: int) -> None:
    counter = 0
    data = []

    for i in stream:
        counter += 1
        data.append(i)
        data_len = len(data)

        if data_len > seq_len:
            del data[0]

        data_len = len(data)

        if data_len == seq_len:
            if data_len == len(set(data)):
                print(f"For seq ({seq_len}): {counter} ({''.join(data)})")
                break


if __name__ == '__main__':
    find_marker(example_stream, 4)
    find_marker(stream, 4)
    find_marker(example_stream, 14)
    find_marker(stream, 14)