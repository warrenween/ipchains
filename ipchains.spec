%define		_scriptver	1.1.2
Summary:	IP firewall and accounting administration tool
Summary(es):	Herramienta para administraci�n de reglas de firewall
Summary(pl):	Narz�dzie do zarz�dzania filtrem pakiet�w IP
Summary(pt_BR):	Ferramentas para gerenciamento de regras de firewall
Summary(ru):	������� ��� ���������� ��������� ��������� ���� Linux
Summary(uk):	���̦�� ��� ��������� ��������� Ʀ������� ���� Linux
Summary(zh_CN):	Linux IPv4����ǽ
Name:		ipchains
Version:	1.3.10
Release:	19
License:	GPL
Group:		Applications/System
Source0:	http://www.netfilter.org/ipchains/%{name}-%{version}.tar.gz
# Source0-md5:	44b6df672a6e7bce8902dc67aef6b12a
#Source1:	http://netfilter.filewatcher.org/ipchains/%{name}-HOWTOs-1.0.7.tar.bz2
Source1:	%{name}-HOWTOs-1.0.7.tar.bz2
# Source1-md5:	f4548c7fb6cdfc1015012c8860a5856a
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source2-md5:	460a8227af67f289ac9868706cf89e54
Source3:	http://people.netfilter.org/~rusty/ipchains/%{name}-scripts-%{_scriptver}.tar.gz
# Source3-md5:	c8996aef5985bddf80844b12ae833781
Patch0:		%{name}-fixman.patch
Patch1:		%{name}-vlanallowing.patch
URL:		http://people.netfilter.org/~rusty/ipchains/
Provides:	firewall-userspace-tool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr
%define		_sbindir	/sbin

%description
This is the Linux IP Firewalling Chains accounting and administration
tool.

Linux IP Firewalling Chains is an update to (and hopefully an
improvement upon) the normal Linux Firewalling code, for 2.2 and 2.3
kernels.

%description -l es
Herramienta para administraci�n de reglas de firewall.

%description -l pl
W j�drach 2.2.xxx/2.3 filtr IP zosta� znacznie zmodyfikowany (i,
miejmy nadziej�, ulepszony). Ipchains (zast�puj�c dawny ipfwadm) s�u�y
do konfigurowania filtru oraz mechanizm�w logowania przychodz�cych
pakiet�w.

%description -l pt_BR
O ipchains do Linux � uma atualiza��o (e esperamos uma melhoria em
rela��o) ao c�digo normal de firewall do Linux, para os kernels 2.0,
2.1 e 2.2. Elas lhe permitem usar firewalls, mascaramento IP, etc.

%description -l ru
Linux IP Firewalling Chains - ��� ����� ����� ������ ��� ����������
��������� ��������� ���� Linux. Ipchains ��������� ��������� firewall,
IP masquerading � �.�.

%description -l uk
Linux IP Firewalling Chains - �� ����� ��¦� ���̦� ��� ���������
��������� Ʀ������� ���� Linux. Ipchains ���������� ����������
firewall, IP masquerading � �.�.

%package -n libipfwc
Summary:	Library which manipulates firewall rules
Summary(pl):	Biblioteka do manipulacji regu�ami filtrowania
Version:	0.2
Group:		Development/Libraries

%description -n libipfwc
Library which manipulates firewall rules.

%description -n libipfwc -l pl
Biblioteka do manipulacji regu�ami filtrowania.

%prep
%setup -q -a1 -a3
%patch -p1
%patch1 -p1

%build
rm -f ipchains
%{__make} -C libipfwc clean
ln -sf %{name}-HOWTOs-1.0.7	doc

%{__make} COPTS="%{rpmcflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_bindir},%{_mandir}/man{4,8}} \
	$RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install ipchains	$RPM_BUILD_ROOT%{_sbindir}
install *.4		$RPM_BUILD_ROOT%{_mandir}/man4
install *.8		$RPM_BUILD_ROOT%{_mandir}/man8
install libipfwc/*.a	$RPM_BUILD_ROOT%{_libdir}
install libipfwc/*.h	$RPM_BUILD_ROOT%{_includedir}
cd %{name}-scripts-%{_scriptver}
install ipchains-restore	$RPM_BUILD_ROOT%{_sbindir}
install ipchains-save		$RPM_BUILD_ROOT%{_sbindir}
install ipfwadm-wrapper		$RPM_BUILD_ROOT%{_sbindir}
install *.8			$RPM_BUILD_ROOT%{_mandir}/man8

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/HOWTO.txt README doc/*.html
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
%lang(es) %{_mandir}/es/man?/*
%lang(it) %{_mandir}/it/man?/*
%lang(ja) %{_mandir}/ja/man?/*
%lang(pl) %{_mandir}/pl/man?/*

%files -n libipfwc
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
