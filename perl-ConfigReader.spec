%include	/usr/lib/rpm/macros.perl
Summary:	ConfigReader perl module
Summary(pl):	Modu� perla ConfigReader
Name:		perl-ConfigReader
Version:	0.5
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/ConfigReader/ConfigReader-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ConfigReader module for perl.

%description -l pl
Modu� perla ConfigReader.

%prep
%setup -q -n ConfigReader-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d	$RPM_BUILD_ROOT%{perl_sitelib}/ConfigReader
install *.pm	$RPM_BUILD_ROOT%{perl_sitelib}/ConfigReader

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/ConfigReader
